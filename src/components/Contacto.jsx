import { MapIcon, Phone, Clock} from "lucide-react"
import "./Contacto.css"

export const Contacto = () => {
  return (
    <section className='contacto-section' id="contacto">
        <h2 className="contacto-titulo">Contáctanos</h2>
        <div className="informacion-container">
            <div className="informacion-item">
                <MapIcon></MapIcon>
                <h3 className="titulo-informacion">Ubicacion</h3>
                <p className="texto-informacion">Av. Principal 123 <br />Ciudad, País</p>
            </div>
            <div className="informacion-item">
                <Phone></Phone>
                <h3 className="titulo-informacion">Telefono</h3>
                <p className="texto-informacion">+54 11 1234-5678</p>
            </div>
            <div className="informacion-item">
                <Clock></Clock>
                <h3 className="titulo-informacion">Horarios</h3>
                <p className="texto-informacion">Lun - Dom <br />11:00 - 23:00</p>
            </div>
        </div>
    </section>
  )
}
