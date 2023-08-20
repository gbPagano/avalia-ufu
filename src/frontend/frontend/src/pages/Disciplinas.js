import { useState, useEffect } from 'react';
import Disciplina from '../components/Disciplina'

export default function Disciplinas(){
    const apiUrl = "http://127.0.0.1:8000/discs";

    const [data, setData] = useState([]);

    const fetchInfo = () => {
        return fetch(apiUrl)
                .then((res) => {return res.json()})
                .then((data) => setData(data))
    }

    useEffect(() => {
        fetchInfo();
    }, []);

    return (
        <div>
            <h1>Disciplinas</h1>
            {data.map((disciplina) =>
            {
                return (
                    <div className="card-disciplina">
                        <h2>{disciplina.nome}</h2>
                        <span>
                            <h4 style={{display: "inline"}}>Dificuldade média: </h4>
                            <p style={{display: "inline"}}>{disciplina.dif_media}</p>
                        </span>
                        <p>Professores lecionando:
                            <ul>
                                {disciplina.professores_desta.map(prof => 
                                        <><li>{prof.nome}</li></>
                                )}
                            </ul> 
                        </p>
                    </div>
                );
            })}
        </div>
    );
}