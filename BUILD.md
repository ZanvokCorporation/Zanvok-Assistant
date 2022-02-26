# Zanvok Assistant 

## Building Zanvok Assistant WHL Package :

  This is the file structure:
  
  ![File Structure](https://user-images.githubusercontent.com/74700000/155846291-d03f708e-33f2-48bb-9975-54b872ec5674.png)
  
  
  * First open command prompt in Windows or Terminal Emulator in Linux
  
  * Then type the command `python setup.py bdist_wheel` in Windows and `python3 setup.py bdist_wheel` in Linux
   
  * After the above command gets executed, type `cd dist` for both Windows and Linux
   
  * Then type `check-wheel-contents` for both Windows and Linux, if you don't have check-wheel-contents module installed, install it with `pip install check-wheel-contents` for Windows and `pip3 install check-wheel-contents` for Linux.
  
  * Hooray you have now created a .WHL package successfully
