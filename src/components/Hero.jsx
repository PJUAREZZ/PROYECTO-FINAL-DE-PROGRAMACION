import "./Hero.css"

export const Hero = () => {
  return (
    <>
        <section className='hero-section' id="inicio">
            <h1 className='hero-titulo'>Bienvenido a Bar & Grill</h1>
            <p className='hero-parrafo'>Las mejores pizzas, sandwiches y wraps de la ciudad. Frescura y calidad en cada bocado.</p>
            <div className="secciones-container">
                <a href="#menu" className="boton-primario">Ver menu</a>
                <a href="#contacto" className="boton-secundario">Contactanos</a>
            </div>
        </section>
        <div className="banner">
            🚚 Envío GRATIS en compras superiores a $25,000
        </div>
    </>
    
    
  )
}
