import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy.io import arff
from sklearn.preprocessing import LabelEncoder
import os
from sklearn import tree

class SimplifiedDataMiningApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Mining Tool")
        self.root.geometry("800x550")
        self.root.configure(bg="#f5f5f5")
        
        self.data = None
        self.create_main_layout()
        
    def create_main_layout(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        header_label = ttk.Label(main_frame, text="Data Mining Tool", font=('Arial', 16, 'bold'))
        header_label.pack(pady=(0, 10))
        
        data_frame = ttk.LabelFrame(main_frame, text="Data Input", padding=10)
        data_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.file_label = ttk.Label(data_frame, text="No file loaded")
        self.file_label.pack(side=tk.LEFT, fill=tk.X, expand=True)
        
        browse_btn = ttk.Button(data_frame, text="Load ARFF File", command=self.load_file)
        browse_btn.pack(side=tk.RIGHT)
        
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        self.clustering_tab = ttk.Frame(self.notebook, padding=10)
        self.classification_tab = ttk.Frame(self.notebook, padding=10)
        
        self.notebook.add(self.clustering_tab, text="Clustering")
        self.notebook.add(self.classification_tab, text="Classification")
        
        self.setup_clustering_tab()
        self.setup_classification_tab()
        
        self.status_var = tk.StringVar(value="Ready")
        status_bar = ttk.Label(self.root, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def setup_clustering_tab(self):
        controls_frame = ttk.Frame(self.clustering_tab)
        controls_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        ttk.Label(controls_frame, text="Feature 1:").pack(anchor=tk.W, pady=2)
        self.feature1_var = tk.StringVar()
        self.feature1_cb = ttk.Combobox(controls_frame, textvariable=self.feature1_var, state="readonly")
        self.feature1_cb.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(controls_frame, text="Feature 2:").pack(anchor=tk.W, pady=2)
        self.feature2_var = tk.StringVar()
        self.feature2_cb = ttk.Combobox(controls_frame, textvariable=self.feature2_var, state="readonly")
        self.feature2_cb.pack(fill=tk.X, pady=(0, 5))
        
        ttk.Label(controls_frame, text="Number of clusters (k):").pack(anchor=tk.W, pady=2)
        self.k_var = tk.StringVar(value="3")
        ttk.Spinbox(controls_frame, from_=2, to=10, textvariable=self.k_var, width=5).pack(fill=tk.X, pady=(0, 10))
        
        self.cluster_btn = ttk.Button(controls_frame, text="Run Clustering", command=self.perform_clustering, state=tk.DISABLED)
        self.cluster_btn.pack(fill=tk.X, pady=10)
        
        self.cluster_frame = ttk.LabelFrame(self.clustering_tab, text="Clustering Result")
        self.cluster_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    
    def setup_classification_tab(self):
        controls_frame = ttk.Frame(self.classification_tab)
        controls_frame.pack(side=tk.LEFT, fill=tk.Y, padx=(0, 10))
        
        ttk.Label(controls_frame, text="Target Variable:").pack(anchor=tk.W, pady=2)
        self.target_var = tk.StringVar()
        self.target_cb = ttk.Combobox(controls_frame, textvariable=self.target_var, state="readonly")
        self.target_cb.pack(fill=tk.X, pady=(0, 10))
        
        self.classify_btn = ttk.Button(controls_frame, text="Run Classification", command=self.perform_classification, state=tk.DISABLED)
        self.classify_btn.pack(fill=tk.X, pady=10)
        
        self.results_frame = ttk.LabelFrame(self.classification_tab, text="Classification Results")
        self.results_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        self.results_text = tk.Text(self.results_frame, wrap=tk.WORD, height=20, width=40)
        self.results_text.pack(fill=tk.BOTH, expand=True)
        self.results_text.insert(tk.END, "Classification results will appear here")
        self.results_text.config(state=tk.DISABLED)
    
    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("ARFF files", "*.arff")])
        if not file_path:
            return
            
        try:
            self.status_var.set("Loading file...")
            self.root.update()
            
            data, meta = arff.loadarff(file_path)
            self.data = pd.DataFrame(data)
            
            for column in self.data.select_dtypes([object]).columns:
                try:
                    self.data[column] = self.data[column].str.decode('utf-8')
                except:
                    pass
                
            for column in self.data.select_dtypes([object]).columns:
                self.data[column] = LabelEncoder().fit_transform(self.data[column].astype(str))
            
            self.file_label.config(text=f"Loaded: {os.path.basename(file_path)} ({len(self.data)} rows)")
            
            self.update_dropdowns()
            
            self.cluster_btn["state"] = tk.NORMAL
            self.classify_btn["state"] = tk.NORMAL
            
            self.status_var.set("File loaded successfully")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load file: {e}")
            self.status_var.set("Error loading file")
    
    def update_dropdowns(self):
        if self.data is not None:
            columns = self.data.columns.tolist()
            numeric_cols = self.data.select_dtypes(include=['float64', 'int64']).columns.tolist()

            self.feature1_cb['values'] = numeric_cols
            self.feature2_cb['values'] = numeric_cols
            self.target_cb['values'] = columns
            
            if numeric_cols:
                self.feature1_cb.current(0)
                self.feature2_cb.current(min(1, len(numeric_cols)-1))
            
            if columns:
                self.target_cb.current(len(columns)-1)
    
    def perform_clustering(self):
        if self.data is None:
            return
        
        col1 = self.feature1_var.get()
        col2 = self.feature2_var.get()
        
        if not col1 or not col2:
            messagebox.showinfo("Info", "Please select both features")
            return
            
        try:
            k = int(self.k_var.get())
            
            for widget in self.cluster_frame.winfo_children():
                widget.destroy()
                
            features = self.data[[col1, col2]].copy().dropna()
            
            self.status_var.set("Running KMeans clustering...")
            #? self.root.update()
            
            kmeans = KMeans(n_clusters=k, random_state=42)
            clusters = kmeans.fit_predict(features)
            
            fig, ax = plt.subplots(figsize=(5, 4))
            scatter = ax.scatter(features[col1], features[col2], c=clusters, cmap='viridis', alpha=0.8)
            
            ax.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], 
                      s=150, marker='X', c='red', label='Centroids')
            
            ax.set_xlabel(col1)
            ax.set_ylabel(col2)
            ax.set_title(f'K-Means Clustering (k={k})')
            ax.legend()
            plt.tight_layout()
            
            canvas = FigureCanvasTkAgg(fig, master=self.cluster_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
            self.status_var.set("Clustering completed")
            
        except Exception as e:
            messagebox.showerror("Error", f"Clustering failed: {e}")
            self.status_var.set("Clustering failed")
    
    def perform_classification(self):
        if self.data is None:
            return
            
        target_col = self.target_var.get()
        
        if not target_col:
            messagebox.showinfo("Info", "Please select a target variable")
            return
            
        try:
            self.status_var.set("Running classification...")
            #? self.root.update()
            
            X = self.data.drop(columns=[target_col])
            X = X.select_dtypes(include=['float64', 'int64']) 
            y = self.data[target_col]
            
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
            
            clf = DecisionTreeClassifier(max_depth=5, random_state=42)
            clf.fit(X_train, y_train)
            
            predictions = clf.predict(X_test)
            accuracy = accuracy_score(y_test, predictions)
            
            report = classification_report(y_test, predictions, zero_division=0)
            
            self.results_text.config(state=tk.NORMAL)
            self.results_text.delete(1.0, tk.END)
            self.results_text.insert(tk.END, f"Decision Tree Classification Results\n\n")
            self.results_text.insert(tk.END, f"Features: {', '.join(X.columns)}\n\n")
            self.results_text.insert(tk.END, f"Target: {target_col}\n\n")
            self.results_text.insert(tk.END, f"Accuracy: {accuracy:.4f}\n\n")
            self.results_text.insert(tk.END, f"Classification Report:\n{report}")
            
            class_counts = y_train.value_counts()
            if len(class_counts) > 1 and class_counts.min() < 5:
                self.results_text.insert(tk.END, "\n\nWarning: Some classes have very few samples, which may affect classification performance.")
            
            plt.figure(figsize=(12, 8))
            feature_names = X.columns.tolist()
            class_names = [str(c) for c in clf.classes_]
            tree.plot_tree(clf, 
                          feature_names=feature_names, 
                          class_names=class_names, 
                          filled=True, 
                          rounded=True)
            plt.tight_layout()
            plt.savefig("decision_tree.png", dpi=300, bbox_inches='tight')
            plt.close()
            
            self.results_text.insert(tk.END, "\n\nDecision tree visualization saved as 'decision_tree.png'")
            self.results_text.config(state=tk.DISABLED)
            self.status_var.set("Classification completed")
            
        except Exception as e:
            messagebox.showerror("Error", f"Classification failed: {e}")
            self.status_var.set("Classification failed")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimplifiedDataMiningApp(root)
    root.mainloop()