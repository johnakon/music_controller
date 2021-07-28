import React, {Component} from "react";
import {render} from  "react-dom";
import HomePage from "./HomePage";



// export default class App extends Component{
//     constructor(props){
//         super(props);
//     }

//     render(){
//         return (<h1>Test Website</h1>)
//     }
// }


const App = (props) => {
    return (
        <div>
            <HomePage />
        </div>
    )
}

export default App


const appDiv = document.getElementById("app");
render(<App />, appDiv);