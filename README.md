<html>

<head>

</head>

<body>
    <h1>Encrpyt the image, binary or text file and calculate before and after the entropy of the File</h1>
    <h2>Installation, set up and Technology for the Project</h2>
    <ul>
        <li>Language - Python 3.8.3</li>
        <li>Libraries - Scipy, Collection, Crypto</li>
    </ul>
    <h2>Command for installing these libraries and running the program</h2>
    <ul>
        <li>pip install scipy</li>
        <li>pip install crypto</li>
        <li>python ./AES_encryption.py</li>
    </ul>
    <h2>Description</h2>
    <p>This project takes large input file(image,binary or text) and apply standard AES encrytion algorithm and covert
        into encrypted file.After that, using entropy method of crpto library calculate the entropy of the file.
    </p>
    <p>Project uses two functions. First one is <b>calculate_entropy</b> and second is <b>main</b> function</p>
    <h3>calculate_entropy function</h3>
    <p>This function takes bytes of data as argument returns the entropy of file in integer</p>
    <ol>
        <li>calculate the frequency of data and store them in to bases variable</li>
        <li>normalize bases variable by dividing every value with sum of bases</li>
        <li>Using standard scipy library function of entropy find entropy and return</li>
    </ol>
    <br/>

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
    </ol>



</body>

</html>
