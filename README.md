## Similarity Search Methods

Similarity search methods help identify data points that are closest to a given query based on their meaning. Below is a breakdown of common similarity search types and the metrics they use:

### Types of Similarity Search

1. **Cosine Similarity Search**  
   - **What it does**: Measures the angle between two vectors (representations of the query and data point).  
   - **Metric used**: Cosine similarity (ranges from -1 to 1). Higher values indicate more similarity.  
   - **Use case**: Ideal for comparing text documents or sentences where the vector magnitudes are less important.

2. **Euclidean Distance Search**  
   - **What it does**: Measures the straight-line distance between two vectors.  
   - **Metric used**: Euclidean distance. Smaller distances indicate closer matches.  
   - **Use case**: Commonly used for image similarity, where vectors represent features of images.

3. **Manhattan Distance Search**  
   - **What it does**: Measures the sum of the absolute differences between two vectors.  
   - **Metric used**: Manhattan distance. It can be faster than Euclidean in some cases.  
   - **Use case**: Useful for grid-based systems, such as pixel comparisons or certain text features.

4. **Jaccard Similarity Search**  
   - **What it does**: Compares the similarity of two sets by evaluating the size of their intersection relative to their union.  
   - **Metric used**: Jaccard index (ranges from 0 to 1). Higher values indicate more similarity.  
   - **Use case**: Works well for comparing sets, such as document similarity based on shared keywords.
