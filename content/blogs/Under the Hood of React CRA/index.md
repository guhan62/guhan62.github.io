---
title: "Under the Hood of React CRA"
date: 2020-08-13T18:58:06-04:00
draft: false
categories: ['guide', 'react']
robotsdisallow: false
---

## React Engine - Intro
*If you are aware of Webpack & Babel, I suggest you [skip to the code part](#wiring-the-code) to set your own minimal React Server*  

[React CRA (Create-React-App)](https://github.com/facebook/create-react-app), is a great package for devs getting started on React.   
It has the all the parts - **loaders, configs, builds, templates, plugins** - It is bootstrapped package for you, to get started working on your React App. It is recommended for everyone, who wants to learn React quick and people looking to learn their first JS framework.   
However, if you are completely new to the web-framework and have **_no-idea_** regarding bundlers, loaders then it is good to have a small peek under the hood, on how to get started with a smaller subset of tools.  

## Before you pop the hood
**This guide is a simple setup, to understand Webpack & Babel how they sync with React**  
* If you want to disassemble and see the functioning of every part of the React engine, then I would suggest looking at [Bohdahn's](https://github.com/Bogdan-Lyashenko) write-up on [Under the hood: React](https://github.com/Bogdan-Lyashenko/Under-the-hood-ReactJS). He has explained the Tree for both v15 & v16, many lifecycle methods deprecated but he summarized and explained the concepts neatly.

* If you are looking for a simpler, neat and quick explanation for React Lifecycle Methods, Check out [Scott Domes's articles on Medium](https://blog.bitsrc.io/react-16-lifecycle-methods-how-and-when-to-use-them-f4ad31fb2282). They come with examples and will get you on track soon.

* So what shall we be doing is, just not adding bloat to our car - we just add what is required and understand how these parts support each other. For that we need many important parts. Let's **pop the hood**.

## The core parts of the React Dev Engine

{{< img src="./React_Components_Apart_proc.jpeg" 
	title="Components that powers React Applications" caption="Image Credits: WikiMedia Commons &" attr="Ben Mullins(Unsplash)" attrlink="https://unsplash.com/@benmullins?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText"
	>}}

* **ES6** - ECMAScript or ES is is a JavaScript standard meant to ensure the compatability of Web pages across different Web browsers. It is popularly used in Node.js programming. Currently, ES2020 is the standard, you can refer to it's [changelog](https://developer.mozilla.org/en-US/docs/Archive/Web/JavaScript/New_in_JavaScript) to understand the evoultion of JS.  
Refer [ECMA Wiki](https://en.wikipedia.org/wiki/ECMAScript) & [ECMA Language Specs](https://tc39.es/ecma262/)

* **Babel** - It is JS toolchain used to convert [ECMAScript](https://en.wikipedia.org/wiki/ECMAScript) 2015+ code into a backwards compatible version of JS for current and older environments. For example,  
    ```javascript
    // Try Babel REPL - https://babeljs.io/docs/en/index.html

    // Babel Input: ES2015+ arrow function, let keyword
    let planets = ['Magrathea', 'Bethselamin', 'Betelgeuse V', 'Earth']
    planets.map(planet => Destroy(planet));

    //  Babel Output: ES5 equivalent
    "use strict";
    var planets = ['Magrathea', 'Bethselamin', 'Betelgeuse V', 'Earth'];
    planets.map(function (planet) {
        return Destroy(planet);
    });
    ```
    Refer [Babel Docs](https://babeljs.io/docs/en/index.html)

* **Webpack** - One of the most intersting tools you will find, webpack is also a JS toolchain that compiles JS modules and bundles them. This bundler combines your code and it's dependencies and puts them together in a file, which can be deployed easily. There are many core concepts to look into, to understand how Webpack bundles the modules using it's dependency graph. Webpack would be the structure that binds all the other parts, will be looking into more of it below.
Refer [Webpack Docs](https://webpack.js.org/guides/getting-started/).

* **CSS Loader, Style Loader** - interprets `@import` and `url()` like `import/require()` and will resolve them. This is a plugin for webpack to resolve your imports on style sheets. The usual trick is including them with a `<link>` in html, but in JS when you call on import statements
    ```javascript
    import css from 'file.css';
    ```
    this URL needs to be resolved by the bundler, which we will configure by installing this additional plugin. As for Style Loaders it is simple injection into DOM.

* **ReactJS** - JS Library for building UI components. Open-Source and maintained by Facebook with a very vibrant community. On v16 now, it has a decent learning curve compared to the other frameworks. There are countless tutorials to learn React from the internet, it is a very useful framework to code up your front-end with actual JS code and offers tons of features like components, states, virtualDOM & lifecycle methods.  
Refer [React Tutorial](https://reactjs.org/tutorial/tutorial.html) and [React Docs](https://reactjs.org/docs/getting-started.html).

## Building the Car

#### Install all the packages and dependenices

```Bash
# Install the following as global deps [if required] ... [the/path/node/node_modules]
npm i react react-dom

# Install the other packages as local deps ... [./node_modules/]
npm i -D @babel/core @babel/preset-env @babel/preset-react core-js \
babel-loader css-loader style-loader html-webpack-plugin webpack webpack-cli webpack-dev-server
```
Refer [npm-install docs](https://docs.npmjs.com/cli-commands/install.html) to understand the arguments.

* **react, react-dom** - React JS packages, to define the functionality of React components and Render methods for virtual DOM.
* **@babel/core, @babel/preset-env, @babel/preset-react, core-js** -   
All Babel packages used here are part of v7, The core functionality for Babel, JSX Rendering & Preset Environments to choose target platforms in verbose terms. But, Core-JS what's that, Babel is pulling the plug on @babel/pollyfill, Pollyfill emulates an ES5+ environment in your code to give you rich feature-set like   
`Promises` - to trigger AJAX queries and safer way to handle req/resp,  
`Array.from` - static method to create an array from an iterable object.
{{< img src="babel[7.4]Pollyfill_Alternative_aug_20_proc.jpeg" title="Babel pulls the plug on @babel/pollyfill">}}
Refer [Babel/Pollyfill](https://babeljs.io/docs/en/babel-polyfill)

* **core-js** - collection of Polyfills to support stable and experimental features of the latest ECMAScript. There are various versions preloaded with the package.  
Refer [Core-Js](https://github.com/zloirock/core-js)

* **regenerator-runtime** - Package to support generator functions and async/await functions. The `regenerator-runtime` package is installed as a dependency and can be found in the `package-lock.json`.

* **html-webpack-plugin** - Webpack plugin to simplify creation of HTML files to serve your webpack bundles. 

* **webpack, webpack-cli, webpack-dev-server** - The simplest and easiest to understand bundler plus easily cutomizable. `webpack-cli` helps environment to play with webpack.config.js, if you want to play arounf yourself additional dependencies need to be installed.  
`webpack-dev-server` one's favourite in developing their web-applications, the content is served on a Node backed server with hot reloads which again is customizable.  
Refer [webpack-dev-server](https://webpack.js.org/configuration/dev-server/)

#### Wiring the code
* Static Files (HTML) & React Boilerplate Code - When you install create-react-app, it gives you an amazing template but bloated service-workers and hidden configs that are managed by react-scripts. Now we must present our own template, below is the structure of our sample application.  
Refer [HTML Guide](https://www.websiteplanet.com/blog/html-guide-beginners/) - if you are a beginner in Coding. **:point_left: Feedback from a Reader**
```Bash
project_folder/
    ├── dist
    │ ├── bundle.js
    │ └── index.html
    ├── index.html
    ├── node_modules
    │.....
    ├── package-lock.json
    ├── public
    │ ├── favicon.ico
    │ └── index.html
    ├── src
    │ ├── css
    │ └── style.css
    │ └── js
    │     ├── App.js
    │     └── index.js
    └── webpack.config.js
``` 

* `App.js, index.js, public/index.html` will be part of our React boilerplate, our boilerplate will be bloated with some ES5+ goodies just to test the functionality of Babel interpreter and webpack bundler.
    _**public/index.html**_
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8" />
        <link rel="icon" href="/favicon.ico" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <meta name="theme-color" content="#000000" />
        <meta
            name="description"
            content="React Template"
        />
    <title>My React App</title>
    </head>
    <body>
        <noscript>You need to enable JavaScript to run this app.</noscript>
        <div id="root"></div>
    </body>
    </html>
    ```
    _**src/js/index.js**_ - It is essential we import both `core-js`, `regenerator-runtime` in the root of our application in the `index.js` but it's play in bundling is handled by the preset we allow in Babel.

    ```react
    import 'core-js';
    import 'regenerator-runtime/runtime';

    import React from "react";
    import ReactDOM from "react-dom";

    import App from './App.js'

    ReactDOM.render(
	<App />,
	document.getElementById('root'));
    ```

    _**src/js/App.js**_ - A simple App with ES6+ modern syntax with the usage of Promises, async/await. Just to test the features of our template out.

    ```react
    import React from "react";
    import '../css/style.css';

    let questions = [
        {'Q' : 'The Infinite Improbability Drive powers Startship? Can it hyperjump to'},
        {'Q' : 'What about '}
    ]
    let swapi = 'https://swapi.dev/api/';
    // async/await JS API function example
    async function getPlanets() {
        const resp = await fetch(swapi+'planets');
        const data = await resp.json();
        return data;                
    };
    // Our React App component
    function App () {
        // Simple State Example
        const [planets, setPlanets] = React.useState([]);
        // Changing State using `useEffect()`
        React.useEffect(() => {
            getPlanets().then(data => {
                //Unpacking the JSON and loading to State
                const planets_data = data.results.map((planet) => {return planet.name})
                setPlanets(planets_data)
            });
        }, []);
        return (
            <div>
            <h1>Starship - Heart of Gold</h1>
                // Template Literals from ES5 - 
                // https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals
                { questions.map((question, idx) => { return(
                    <h2 key={idx}>{`${question.Q} ${planets[idx]}?`}</h2>) 
                    })
                } 
            </div>
        )
    }
    export default App
    ```
* Now the tricky part to write our `webpack config` in `webpack.config.js`
    ```JavaScript
    // 1 - Packages required
    var HtmlWebpackPlugin = require('html-webpack-plugin');
    var path = require('path');

    // 2 - Webpack Concepts [Entry, Output, Loaders, plugins]
    module.exports = {
        entry: path.resolve( __dirname,'src/js/index.js'),
        output: {
            path: path.resolve( __dirname, 'dist/'),
            filename: 'bundle.js'
        },
    
    module : {
        rules: [
            {
               test: /\.css$/i,
                use: [
                    { loader: "style-loader" },
                    { loader: "css-loader" }
                ]
            }, 
            {
                test: /\.m?(js|jsx)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: { presets :['@babel/preset-env', "@babel/preset-react" ]}
                    }
            }
        ]
    },
    plugins:[ new HtmlWebpackPlugin({
        template: path.resolve( __dirname, 'public/index.html'),
        filename: 'index.html',
        favicon : 'public/favicon.ico'  }) 
    ],
    devServer : {
        inline: false,
        hot: true
    }
    }
    ```
    1. **Packages required** : html-webpack-plugin is an external package that must be imported to be used, we use the Node package path to resolve paths.
    2. **Webpack Concepts** : 
        * **Entry** : Entry-Point of our Application or root node to the dependency graph of Webpack, here `src/js/index.js`
        * **Output**: After bundling the modules, emitting the final bundle to specified directory, in our case `/dist/bundle.js`.
        * **module.rules** : Specifying rules for certain files in project folder which `loader` is to be used and additional options specified.
        * **plugins** : Additional capabilities (self-developed packages / 3rd party) to optimize or tweak your webpack process.
        * **devServer**: Additional Dev Server Capabilities

    **Refer the Docs, to understand more on Webpack** : [Webpack Concepts](https://webpack.js.org/concepts/)

* Finally to include some Babel config and few CLI tricks in your `package.json`. Add a `key` for `Babel config`, to configure presets for ES environment emulation.
    ```json
    "babel": {
        "presets": [
        ["@babel/preset-env", {
            "useBuiltIns": "usage",
            "corejs": "3.6"}
        ]
    ]
    }
    ```
    Also modify your `scripts` key in you `package.json`,
    ```json
    "scripts": {
        "build:dev": "webpack --mode=development",
        "start": "webpack-dev-server  --mode development",
    }
    ```
* Run the command `npm start` and navigate to `localhost:8080` if you want to give a specified port check out [dev-server](https://webpack.js.org/configuration/dev-server/) to add the `port` property to `devServer` in your `webpack.config.js`
{{< img src="React_Template_proc.jpeg" title="Our Simple React Template demonstrating minimum ES5+ code using Webpack config">}}

## Key Takeaways
* Now, you get to understand the picture how `Webpack`, `Babel` & `React` are the brains behind the React CRA.
* React CRA is wonderful, it is good to understand how does the framework powers itself.
* Breaking apart the webpack config, understanding modules & plugins.
* Pollyfill replacement with core-js and how to set the environment.