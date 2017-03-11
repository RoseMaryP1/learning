Question
------

You are given a collection of 1 million images provided by a customer. The images are pictures of multiple items this customer sells on her website (like chairs, shoes, computers, etc). The customer wants us to build a system for her to search over these images repeatedly.

To clarify what we mean by above search, let’s denote the collection of all these images by I. Search means given an image P from collection I, return top N images that look “visually similar” to P.  Remember we are asked to do the searches repeatedly, and searches will power a website, so each individual search should be fast. 

Outline briefly (in a paragraph or two) how you would go about building such a system. What criteria would use for visual similarity? How would you make sure the searches are fast enough? How would you make sure the system you are going build actually works?


Answers
=====

How I would build it
----------

First, we'd need a way to index the images given and extract features. I would probably pre-process them with an existing deep network, say Inceptionv3 without last few layers (softmax) to get more generic features. We'd get say 1024 features out that we could then index along with the image name. We could use something like KNN to find the N nearest neighbors directly in the feature space, though might not work well with so many images (1M x 1M comparisons to store).

There should certainly be ways to preprocess the images and create good indexes. For instance, we could instead look at indexing images based an embedding or locally sensitive hash over the features we generated for faster retrieval and we wouldn't have to worry about comparing each image to every other one. Might also make sense to index on the cluster that an image is in (bin method?) Since we don't have any labelled data, we could use something like KMeans or Density based clustering to give us a reasonable clusters. I would ensure it works by first ensuring my concepts above are correct, then prototype it with a subsample of the data, probably using Jupyter notebook to create a report of what the actual data looks like and my initial results. I'd also check my assumptions on storage size and processing time for these indexes. 





