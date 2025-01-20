import * as React from 'react'
import '../styles/styles.css'

const Navbar = () => {
    return(
        <nav className="my-4 px-4 flex flex-wrap gap-4">
           {
               // Add more links to array if needed
               [
                   ['Home', '/'],
                   ['About', '/about.html'],
                   ['Contact', '/contact.html'],
                   ['Classes', '/classes.html'],
                   ['Events', '/events.html'], 
               ].map(([ title, url ]) => {
                   return <a href={url} key={title} className="text-lg relative after:absolute after:-bottom-1 after:left-0 after:w-full after:scale-x-0 after:h-[3px] after:rounded-full after:bg-red-700 after:content-[&#32;] hover:after:scale-x-100 after:transition-transform after:duration-300 motion-reduce:transition-none">{title}</a> 
               })
           }
        </nav>
    );
}

export default Navbar