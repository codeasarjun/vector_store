import numpy as np

class  vectorStore:
    def __init__(self):
        self.vector_data={}
        self.vector_index={}
    def add_vector(self,vector_id,vector_data):
        self.vector_data[vector_id]=vector_data
        self.update_index(vector_id, vector_data)
    def get_vector(self,vector_id):
        return self.vector_data.get(vector_id)
    
    def update_index(self,vector_id,vector_data):
        for existing_id, existing_vector in self.vector_data.items():
            similarity = np.dot(vector_data, existing_vector) / (np.linalg.norm(vector_data) * np.linalg.norm(existing_vector))
            if existing_id not in self.vector_index:
                self.vector_index[existing_id] = {}
            self.vector_index[existing_id][vector_id] = similarity

    def find_similar_vector(self,query_vector,num_results=3):
        results=[]
        for vector_id,vector_data in self.vector_data.items():
            similarity = np.dot(query_vector, vector_data) / (np.linalg.norm(query_vector) * np.linalg.norm(vector_data))
            results.append((vector_id, similarity))

        # Sort by similarity in descending order
        results.sort(key=lambda x: x[1], reverse=True)

        # Return the top N results
        return results[:num_results]





