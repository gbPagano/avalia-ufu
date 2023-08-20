import { useState, useEffect } from 'react';
import { BrowserRouter, Link, Route, Routes } from 'react-router-dom';
import ProfPerfil from '../components/ProfPerfil';
import Disciplina from '../components/Disciplina';

export default function Professores(){
    const apiUrl = "http://127.0.0.1:8000/profs";

    const [data, setData] = useState([]);

    const fetchInfo = () => {
        return fetch(apiUrl)
                .then((res) => res.json())
                .then((data) => setData(data))
    }

    useEffect(() => {
        fetchInfo();
    }, []);
    
    return(
        <div>
            <h1>Professores</h1>
            {data.map((dataObj) =>
            {
                return (
                    <div className="card-professor">
                        <h2>{dataObj.nome}</h2>
                        <p>Nota média: {dataObj.nota}</p>
                        <p>Disciplinas lecionadas: 
                            <ul>
                                {dataObj.disciplinas_lecionadas.map(disciplina => 
                                    <>
                                    <li>
                                        <Link to={"/disciplina/" + disciplina.id_disciplina}>
                                            {disciplina.nome}
                                        </Link>
                                    </li>
                                    </>)}
                            </ul>
                        </p>
                    </div>
                );
            })}
        </div>
    );
}