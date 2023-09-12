# goodbytes
A language model for developing recipes

## Setup
This only works on Linux. I recommend Ubunutu 22.04. You also need the correct setup of CUDA and Pytorch. The environment file is set up for CUDA 11.8 and the instructions for installation are here: https://developer.nvidia.com/cuda-11-8-0-download-archive?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local

```
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-ubuntu2204.pin
sudo mv cuda-ubuntu2204.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu2204-11-8-local_11.8.0-520.61.05-1_amd64.deb
sudo cp /var/cuda-repo-ubuntu2204-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
sudo apt-get -y install cuda
```

Once CUDA 11.8 is installed, create the environment using conda/mamba:
```conda env create --file environment.yml```

## Examples

```
from Recipe_Generator import generate_response

generate_response("sugar, flour, salt, butter")
```

Results:
Ingredients: sugar, flour, salt, butter
Full Recipe:
Directions:
1. Preheat oven to 350°F. Line a 9-inch square pan with parchment paper.
2. In a large bowl, combine the sugar, flour, and salt. Cut in the butter until the mixture resembles coarse crumbs.
3. Press the mixture into the prepared pan. Bake for 20 to 25 minutes, or until golden brown. Cool completely before cutting into squares.

Ingredients: chicken, garlic, onion, salt, oil
Full Recipe:
Directions:
1. Preheat oven to 350°F.
2. In a large skillet, heat oil over medium-high heat. Add garlic and onion; cook until tender, about 5 minutes.
3. Add chicken; cook until browned, about 5 minutes.
4. Transfer to a baking sheet. Bake until chicken is cooked through, about 10 minutes.
5. Serve with lemon wedges.
Serves: 4
Prep Time: 15 minutes
Cook Time: 15 minutes
Total Time: 30 minutes