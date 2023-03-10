# Recipe Chooser

Yeah, one more app with recipes. Then why did I create it?

*Reason 1*. It's going to help you in making a decision. Almost every morning we have to come up with breakfast 
ideas before we’ve even had coffee. Sometimes it can feel like a really tall order and annoying.
Using this app you can just save all your recipes, 
and every time you need an idea the app will choose it for you.

*Reason 2*. I need to practice Python.



## Usage

1. You must have [Docker](https://www.docker.com/products/docker-desktop/) installed.
2. Clone the project to your local machine:

    ```
    git clone git@github.com:lenorium/what_to_cook.git
    ```
    or download zip if you don't have Git installed.
3. Open terminal, go to the project directory:
    
    ```
    cd <path>/what_to_cook
    ```
4. Run Docker container:

    ```
    docker-compose up --build -d
    ```
5. When container is up, open your web browser and go to http://0.0.0.0:8000/ or http://127.0.0.1:8000/ (which is most probably if you use Safari). If everything is ok, you'll see text 'It works!'.
6. To see full list of available HTTP methods and try them open docs: http://0.0.0.0:8000/docs (or http://127.0.0.1:8000/docs).

**Additionally**

Also you can see structure of DB tables using PGAdmin:

1. Open http://0.0.0.0:8001/ (or http://127.0.0.1:8001/) in your browser.
2. Enter login and password. You can find it in ```.env``` file. 
3. When dashboard is opened press ```Add New Server``` button.
4. As the name of server you can enter anything you like. 
5. In the tab ```Connection``` in the ```Host``` field input ```db```. Password is the same as in step 2.
6. If everything is ok, you'll see a list of DBs and 'recipes' DB among them.
