# TMM4275-Assignment3

This project is a part of the course TMM4275 Knowledge-Based Enineering, Project. The main task is developing an automatic KBE solution to check and show volumes, where a welding gun can fit in order to make the weld the walls in a maze-like structure. The customer will upload a .prt file containing the maze-lice structure to a website as well as defining what type of welding gun they are using to make the welds. 

This project is made by: 
* Kasper Kallseter
* Magnus Myklegard
* Amalie Berge Holm

### The Maze-like Structure
The image below is an example of how a structure may look. 
![img name](img url)

The cusomer will upload and define: 
* Upload .prt file 
* Define type of nozzle on the welding gun

### The KBE Application Architecture
This is a diagram showing the main blocks and interconnections between them. 

![img name](img url)

The main lines of the KBE architecture are the same as in assignment 1 and 2, where the customer will give inputs on a website, but in stead of setting values for different parameter, as in the previous assignments, the customer will now upload a .prt file as well. In the previous assignments the values have been transfered to a DFA file, which have been uploaded to NX, in this assignment the .prt file is directly uploaded to NX. As in assignment 2, there is no need for a Fuseki server her either, as the constraints are given by the choice of welding gun and that a ".prt" file is the only possible file to upload. 

### ULM Sequence Diagram
The ULM sequence diagram showing how an order making scenario will play out. All the way from how the customer uploading the file to the webage, to the algorithm checking the volumes in NX, and displaying the result back to the customer on a webpage. 

![img name](img url)

In assignment 1 Olingvo and Apache Jena Fuseki were used to communicate with the server containing the parameters, set by both the customer and the product engineer. In assignment 2 the product engineer sat a DFA template which was written to by the DFA server, as well as checking if they are within the room, and not needing a Manufacture Checker Server or a Fuseki Server. Now, in assigment 3 the constrain

Another difference from assignment 1 is that the web browser client now uses three different websites, rather than only one, to get the values from the customer. This makes the sequence diagram more complex on the left hand side for assignment 2 compared to assignment 1. This is the case for assigment three as well, though the structure is not as complex as it was for assigment 2. 

### Development Tools
This code was made using python and HTML in Visual Studio Code, the Flask extension was used as the framework for the webpage. (Knowledge Fusion and Journal was used in NX to make models of the rail.) NX Open was used to make journals, to find the edges and then coloring in the volumes in the maze. NX Oplen was also used to  easily take pictures of the product for every order. 

In assignment 1 Olingvo and Apache Jena Fuseki was used to communicate with the server containing the parameters, as stated above, this was not used in assignment 2 or 3. This is because the constraints are set by the server, in the same place where they are recieved from the customer. 

### Code Description 
- `server.py` - Setting ut the webpage using Flask. Recieving input from the customer and saving it, as well as redirecting to the right html pages
- templates - Folder containing the html pages
  - `index.html` - The first html page the customer sees, where they select type of nozzle on the welding gun and upload the .prt file
  - `uploader.html` - The page returned to the customer when the input has been recieved, redirects the customer back to home page or to the page containing results of the weldability checker
  - `result.html`- The page showing the customer the result of the weldability checker 

- `Weldability.py`- NX Open Journal file finding all the edges in the .prt file 
- `colorMaker.py`- NX Open Journal file coloring in the voumes according to the measurements of the nozzle chosen 
- `volumeChecker.py`- 

- uploadedFiles - Folder where the uploaded .prt file is saved
- static - Folder where the image of the result is saved

## Examples of Three Different Product Orders  

### The Layout of the Web Page the Customer Uses
![img name](img url)

### A Customer Trying to Order Outside the Constraints
![img name](img url)

### Example 1 
![img name](img url) - customer setting input 
![img name](img url) - reviecing result

### Example 2
![img name](img url) - customer setting input 
![img name](img url) - reviecing result

### Example 3
![img name](img url) - customer setting input 
![img name](img url) - reviecing result

### Common Colclusion on Building KBE System based on the tree assignments 

