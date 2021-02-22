# cloud-key-wrapper
Making key wrapping for GCP and AWS easy. 


# Why? 

** Well it's a pain. ** 

So keywrapping in generally looks simple but if you follow the google cloud manual you soon figure out it's time cosuming. 
So instead of setting up openssl locally why not have a ready to go script or service that does the following. 

* steps * 

1. It generates the AES key for you. 
2. It takes the Google cloud public key
3. It wraps and signs the key for you
4. You get the wrapped key and your own AES key back! 

To see if it works you can use the test key from this repo. 

# a general wishlist

1. webinterface
2. a simplefied script that doesn't require the understanding of docker.
