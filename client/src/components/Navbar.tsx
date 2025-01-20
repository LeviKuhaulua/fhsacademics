import * as React from 'react'
import '../styles/styles.css'

const Navbar = () => {
    return(
        <nav className="my-4 px-4 flex flex-wrap gap-4 text-lg font-normal">
           {
               // Add more links to array if needed
               [
                   ['Home', '/'],
                   ['About', '/'],
                   ['Contact', '/'],
                   ['Classes', '/'],
                   ['Events', '/'], 
               ].map(([ title, url ]) => {
                   return <a href={url} key={title}>{title}</a> 
               })
           }
        </nav>
    );
}

export default Navbar