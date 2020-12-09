<html>

<head>

</head>

<body>
    <h1>Encrpyt the image, binary or text file using AES encryption and calculate before and after the entropy of the File</h1>
    <h2>Installation, set up and Technology for the Project</h2>
    <ul>
        <li>Language - Python 3.8.3</li>
        <li>Libraries - Scipy, Collection, Crypto</li>
    </ul>
    <h2>Command for installing these libraries and running the program</h2>
    <ul>
        <li>pip install numpy==1.19.3</li>
        <li>pip install scipy</li>
        <li>pip install crypto</li>
        <li>python AES_encryption.py</li>
    </ul>
    <p>If you are using spyder IDE then install 3 packages as shown above using Ipython console and then run using F5 button.</p>
    <h2>Description</h2>
    <p>This project takes large input file(image,binary or text) and apply standard AES encrytion algorithm and covert
        into encrypted file.After that, using entropy method of crpto library calculate the entropy of the file.
    </p>
    <p>Project uses two functions. First one is <b>calculate_entropy</b> and second is <b>main</b> function</p>
    <img src = "https://github.com/hiteshparate/ITS/blob/main/final_final_gif.gif" alt="gif of encryption"/>
    <h3>calculate_entropy function</h3>
    <p>This function takes bytes of data as argument returns the entropy of file in integer</p>
    <ol>
        <li>calculate the frequency of data and store them in to bases variable</li>
        <li>normalize bases variable by dividing every value with sum of bases</li>
        <li>Using standard scipy library function of entropy find entropy and return</li>
    </ol>
 
<h3> Main Algorithm</h3>
    <ol>
        <li>open file using open() function and give path and read in bytes(rb) as argument</li>
        <li>generate key of using get_random_bytes() function of desired size, here we have used 16 bytes size</li>
        <li>select buffer size, we have chosen 64kb of buffer</li>
        <li>create file and open file using open() function and give write permission</li>
        <li>Create a new cipher using key and give encryption mode(CFB)</li>
        <li>using cipher.encrpyt() function generte encrpted bytes and write them into encrypted file untill input file
            is not completely read</li>
        <li>close input and output file</li>
        <li>To calculate entropy of the file again open file and read files into data bytes call the function
            <b>calculate_entropy</b> to find entropy values</li>
        <li>Change the file_name as "7z.dll" or "image.jpg" or "alice29.txt" and run again for different outputs</li>
    </ol>
  

    


</body>

</html>
