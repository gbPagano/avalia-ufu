import { Link } from "react-router-dom"

export default function Navbar(){
    return (
        <nav className="nav">
            <Link to="/" className="site-title">WikiProf</Link>
            <ul>
                <li><Link to="/professores">Professores</Link></li>
                <li><Link to="/disciplinas">Disciplinas</Link></li>
                <li><Link to="/sobre">Sobre</Link></li>
            </ul>
        </nav>
    );
}