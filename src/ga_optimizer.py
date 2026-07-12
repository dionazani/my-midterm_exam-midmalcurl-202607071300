# src/ga_optimizer.py
import numpy as np
from sklearn.model_selection import cross_val_score

class GeneticAlgorithmFeatureSelector:
    """
    Modul Seleksi Fitur Berbasis Algoritma Genetika (GA).
    """
    def __init__(self, estimator, pop_size=10, generations=5, crossover_rate=0.8, mutation_rate=0.1, random_state=42):
        self.estimator = estimator
        self.pop_size = pop_size
        self.generations = generations
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.random_state = random_state
        np.random.seed(self.random_state)

    def _fitness_function(self, X, y, chromosome):
        """Menghitung fitness berdasarkan F1-Score menggunakan validasi silang."""
        selected_indices = np.where(chromosome == 1)[0]
        if len(selected_indices) == 0:
            return 0.0
            
        X_selected = X[:, selected_indices]
        scores = cross_val_score(self.estimator, X_selected, y, cv=3, scoring='f1', n_jobs=-1)
        return np.mean(scores)

    def fit(self, X, y):
        """Melakukan proses evolusi GA."""
        X_matrix = np.array(X)
        y_vector = np.array(y)
        num_features = X_matrix.shape[1]
        
        # Inisialisasi populasi
        population = np.random.randint(2, size=(self.pop_size, num_features))
        
        best_chromosome = None
        best_fitness_score = -1.0
        
        print(f"Memulai Optimasi GA untuk {self.generations} Generasi...")
        
        for generation in range(self.generations):
            fitness_scores = []
            
            # Evaluasi populasi
            for chromosome in population:
                score = self._fitness_function(X_matrix, y_vector, chromosome)
                fitness_scores.append(score)
                
                # Pembaruan kromosom terbaik
                if score > best_fitness_score:
                    best_fitness_score = score
                    best_chromosome = chromosome.copy()
            
            print(f"Generasi {generation + 1}/{self.generations} | Fitness Terbaik: {best_fitness_score:.4f}")
            
            # (Di sini Anda akan menambahkan logika untuk Seleksi, Crossover, dan Mutasi)
            # Untuk saat ini, kita biarkan simpel untuk demonstrasi.
            
        self.best_chromosome_ = best_chromosome
        self.best_fitness_ = best_fitness_score
        return self