import React, { Component } from 'react';
const element =<h1>Hello! Talhas  UI</h1>
class Counter extends React.Component 
{
    state= 
    { 
        count:1
    };
    handleShowurls=
    {


    };
    styles=
    {
        fontSize:30 ,
        fontWeight: "bold"
    };
  render() { 
    return (
        <div>
            <span style={this.styles} className="badge badge-primary m-1"> Select the option: </span>
            <button onClick={this.handleShowurls} >Show Current URLs</button>
            <button>Enter URL</button>
            <button > Close </button>
        </div>
    );
  }
}
 
export default Counter;
