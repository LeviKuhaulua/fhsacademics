import * as React from 'react'
import '../styles/styles.css'

const Navbar = () => {
    return(
        <nav className="my-4 px-4 flex flex-wrap gap-4 text-lg font-normal">
           {
               // Add more links to array if needed
               [
                   ['Home', '/'],
                   ['About', '/about.html'],
                   ['Contact', '/contact.html'],
                   ['Classes', '/classes.html'],
                   ['Events', '/events.html'], 
               ].map(([ title, url ]) => {
                   return <a href={url} key={title}>{title}</a> 
               })
           }
        </nav>
    );
}

export default Navbar