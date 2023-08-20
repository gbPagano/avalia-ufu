import React, { useState, useEffect } from 'react';
import apiUrl from '../App';


export default function Professores(){
    const apiUrl = "http://127.0.0.1:8000/profs";

    const [data, setData] = useState([]);

    const fetchInfo = () => {
        return fetch(apiUrl)
                .then((res) => {return res.json()})
                .then((data) => setData(data))
    }

    useEffect(() => {
        fetchInfo();
    }, []);
    
    console.log(apiUrl);

    return(
        <div>
            <h1>Professores</h1>
            {data.map((dataObj) =>
            {
                return (
                    <div className="card-professor">
                    <h2>{dataObj.nome}</h2>
                    <p>Nota do professor: {dataObj.nota}</p>
                    <p>Disciplinas lecionadas: {dataObj.disciplinas_lecionadas.map(disciplina => <>{disciplina.nome}</>)}</p>
                    </div>
                );
            })}
        </div>
    );
}