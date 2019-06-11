# cuDNNv: cuDNN Version Switcher (v0.4)

cuDNNv is a simple script to install cuDNN to your system or to change the version of the existing cuDNN to an older/a newer version. Although the script is super simple, it saves you quite a bit of time by reducing a minute long work to a single button click. It especially becomes a life saver if you're working with multiple frameworks that use different versions of cuDNN. cuDNNv currently works only on 64-bit Linux for any cuDNN version.

## Using cuDNNv

1. Clone the repository to your working directory by using the following command:

   ```bash
   git clone https://github.com/dnzzcn/cuDNNv.git
   ```
   Or directly download it as a ZIP file and extract it to any directory you want.

3. Download the cuDNN version you want to use from [NVIDIA Developer page](https://developer.nvidia.com/rdp/form/cudnn-download-survey). You have to login to your account, or create one if you don't already have, in order to download the package. Please make sure that you download the package that is suitable with the CUDA version you use, because it is not being checked by cuDNNv.

4. Move the .tgz file you downloaded from NVIDIA Developer page to 'cuDNNv/packages' folder (or to 'cuDNNv-master/packages' folder, if you downloaded the repository as a ZIP file).

5. Finally, you can run the script by running the following command inside the cuDNNv directory:

   ``` 
   ./cuDNNv &
   ```
   
   You can choose the version you want to install/switch to from the dropdown menu and then click the switch button. You can also use cuDNNv to clean install the version you are already using to make sure it is working properly.
   
## Permission Error

   This error might be encountered if files of a cuDNN version are created with root privileges in an earlier installment. If you happen to have this error, you need to run cuDNNv with root privileges too.
   
   ``` 
   sudo ./cuDNNv &
   ```
