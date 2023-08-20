import { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Review from '../components/Review';

export default function Disciplina(){
    let { id } = useParams();

    const apiUrl = `http://127.0.0.1:8000/discs/${id}`;

    const [disciplina, setDisciplina] = useState([]);

    const fetchInfo = () => {
        return fetch(apiUrl)
                .then((res) => {return res.json()})
                .then((disciplina) => setDisciplina(disciplina))
    }

    useEffect(() => {
        fetchInfo();
    }, []);
    
    console.log(disciplina);

    return (
        <>
        <div className="card-disciplina">
                        <h2>{disciplina.nome}</h2>
                        <span>
                            <h4 style={{display: "inline"}}>Dificuldade média: </h4>
                            <p style={{display: "inline"}}>{disciplina.dif_media}</p>
                        </span>
                        <p>Professores lecionando:
                            <ul>
                                {disciplina.professores_desta != undefined ?
                                    disciplina.professores_desta.map(prof => 
                                        <><li>{prof.nome}</li></>
                                    )
                                    :
                                    <></>
                                }   
                            </ul> 
                        </p>
                        <h3>Reviews:</h3>
                        {disciplina.reviews_desta != undefined ?
                         disciplina.reviews_desta.map(review => <Review review={review} />)
                        :
                        <></>}   
                    </div>
        </>
    );
}