import React, { use } from 'react'
import { useState } from 'react'
import { ShoppingCart, XIcon, MenuIcon, Hamburger } from 'lucide-react'
import "./Navegador.css"

export const Navegador = () => {
    const[carritoOpen, setCarritoOpen] = useState(false)
    const[menuOpen, setMenuOpen] = useState(false)  

    const handleLinkClick = () =>{
      setMenuOpen(false)
    }

  return (

    <header>
        <div className='logo-container'>
            <Hamburger></Hamburger>
            <p>Bar & Grill</p>
        </div>

        <nav>
            <ul className='nav-ul'>
                <li><a href='#inicio' className='nav-li'>Inicio</a></li>
                <li><a href='#menu' className='nav-li'>Menu</a></li>
                <li><a href='#nosotros' className='nav-li'>Nosotros</a></li>
                <li><a href='#contacto' className='nav-li'>Contacto</a></li>
            </ul>
        </nav>

        <div className="actions-container">
            <button className='carrito-button'><ShoppingCart></ShoppingCart></button>
            <button onClick={() => setMenuOpen(!menuOpen)} className='menu-button'>
              {menuOpen ? <XIcon /> : <MenuIcon />}
            </button>
        </div>
        
        {/* Navegador Responsive */}
        {menuOpen && (
            <nav className="nav-mobile">
              <ul className='nav-ul'>
                <li><a href='#inicio' className='nav-li' onClick={handleLinkClick}>Inicio</a></li>
                <li><a href='#menu' className='nav-li' onClick={handleLinkClick}>Menu</a></li>
                <li><a href='#nosotros' className='nav-li' onClick={handleLinkClick}>Nosotros</a></li>
                <li><a href='#contacto' className='nav-li' onClick={handleLinkClick}>Contacto</a></li>
              </ul>
                
            </nav>
          )}

    </header>
  )
}
