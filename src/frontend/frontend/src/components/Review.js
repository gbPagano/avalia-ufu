import { useState, useEffect } from 'react';

export default function Review({ review }){    
    return (
        <div className="card-review">
            <span>
                <h4 style={{display: "inline"}}>Autor: </h4>
                <p style={{display: "inline"}}>{review.autor}</p>
            </span>
            <br />
            <span>
                <h4 style={{display: "inline"}}>Professor: </h4>
                <p style={{display: "inline"}}>{review.professor.nome}</p>
                <p style={{fontStyle: "italic"}}>{review.comentario}</p>
            </span>
            <span>
                <h4 style={{display: "inline"}}>Nota ao professor: </h4>
                <p style={{display: "inline"}}>{review.nota}</p>
            </span>
            <br />
            <span>
                <h4 style={{display: "inline"}}>Dificuldade da disciplina: </h4>
                <p style={{display: "inline"}}>{review.dif_disciplina}</p>
            </span>
            <br />
            <span>
                <h4 style={{display: "inline"}}>Upvotes: </h4>
                <p style={{display: "inline"}}>{review.upvotes}</p>
            </span>
        </div>
    );
}