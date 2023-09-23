import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Review from "../components/Review";
import { BiTachometer } from "react-icons/bi";
import chroma from "chroma-js";

export default function Disciplina() {
  let { id } = useParams();

  const apiUrl = `http://127.0.0.1:8000/discs/${id}`;

  const [disciplina, setDisciplina] = useState();

  useEffect(() => {
    fetchInfo();
  }, []);

  const fetchInfo = async () => {
    return await fetch(apiUrl)
      .then((res) => res.json())
      .then((disciplina) => setDisciplina(disciplina));
  };

  if (disciplina) {
    return (
      <>
        <div class="font-custom p-12 text-white min-h-screen h-fit">
          <h2 class="text-2xl font-custom font-bold text-cyan-100">
            {disciplina.nome}
          </h2>
          <h3 class="text-lg text-cyan-200">{disciplina.faculdade.nome}</h3>
          <div class="p-2">
            <div class="w-full flex gap-1 items-center">
              <BiTachometer class="inline" size={30} color={chroma("gray")} />
              <p class="inline text-green-400 text-lg font-bold">
                {disciplina.dificuldade}
              </p>
            </div>
            <p>Professores lecionando:</p>
            <ul class="p-2 flex flex-row">
              {disciplina.professores_desta !== undefined ? (
                disciplina.professores_desta.map((prof) => (
                  <>
                    <li>
                      <button class="px-4 py-1 text-sm text-white rounded-full border border-gray-500">
                        {prof.nome}
                      </button>
                    </li>
                  </>
                ))
              ) : (
                <></>
              )}
            </ul>
            <h3>Reviews:</h3>
            {disciplina.reviews_desta !== undefined ? (
              disciplina.reviews_desta.map((review) => (
                <Review review={review} />
              ))
            ) : (
              <></>
            )}
          </div>
        </div>
      </>
    );
  }
}
