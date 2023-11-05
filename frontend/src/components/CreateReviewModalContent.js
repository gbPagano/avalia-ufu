import Api from "../api/Api.js";
import { useState } from "react";

export default function CreateReviewModalContent({
  prof,
  discs,
  onClose,
  handleReviewSent,
}) {
  const [profScore, setProfScore] = useState();
  const [difDisc, setDifDisc] = useState();
  const [disc, setDisc] = useState(discs[0].id);
  const [comment, setComment] = useState();

  function handleProfScoreChange(e) {
    setProfScore(e.target.value);
  }

  function handleDifDiscChange(e) {
    setDifDisc(e.target.value);
  }

  function handleDiscChange(e) {
    setDisc(e.target.value);
  }

  function handleCommentChange(e) {
    setComment(e.target.value);
  }

  return (
    <div
      id="create-review-modal"
      class="font-custom flex flex-col h-3/4 gap-4 fixed top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 pt-5 p-6 backdrop-blur-xl bg-opacity-70 z-40 shadow-2xl shadow-black w-1/3 min-w-fit min-h-fit bg-gray-950 rounded-2xl"
    >
      <div id="recipient">
        <h3 class="inline text-white">Enviando uma review para </h3>
        <p class="inline text-cyan-400 font-bold text-xl"> {prof.nome}</p>
      </div>
      <form id="review-form" class="mt-0.5 mb-5 flex flex-col gap-1 h-5/6">
        <div id="review-score" class="p-0 m-0">
          <p class="inline font-semibold text-white">Nota ao professor: </p>
          <input
            onChange={handleProfScoreChange}
            class="inline rounded-3xl pt-1 pb-1 pr-3 pl-2.5 w-16 shadow-md"
            type="number"
            min="1"
            max="10"
            step="1"
          />
        </div>
        <div id="selected_disc">
          <p class="font-semibold inline text-white">Disciplina: </p>
          <select
            onChange={handleDiscChange}
            class="p-1 w-96 rounded-xl shadow-md bg-white"
          >
            {discs !== undefined ? (
              discs.map((disc) => <option value={disc.id}>{disc.nome}</option>)
            ) : (
              <></>
            )}
          </select>
        </div>
        <div id="disc_difficulty" class="w-full">
          <p class="inline font-semibold text-white">
            Dificuldade da disciplina:{" "}
          </p>
          <input
            onChange={handleDifDiscChange}
            class="inline rounded-3xl pl-2.5 pt-1 pb-1 pr-3 w-16 shadow-md"
            type="number"
            min="1"
            max="10"
            step="1"
          />
        </div>
        <div id="review-comment" class="w-full h-full">
          <p class="font-semibold pb-2 text-white">Comentário:</p>
          <textarea
            onChange={handleCommentChange}
            class="w-full h-full rounded-xl p-2 shadow-md"
            placeholder="Digite um comentário respeitoso."
          ></textarea>
        </div>
      </form>
      <div class="flex justify-end gap-6 right-28 pt-3">
        <button
          class="px-5 py-2 text-sm text-white font-bold rounded-full bg-cyan-600 hover:bg-cyan-800"
          onClick={async () => {
            await Api.postReview("autorTeste", prof, disc, {
              comment: comment,
              profScore: profScore,
              discDifficulty: difDisc,
            })
              .then(onClose())
              .then(handleReviewSent(true));
          }}
        >
          Enviar
        </button>
        <button
          class="px-5 py-2 text-sm text-black font-bold rounded-full bg-cyan-100 hover:bg-cyan-200"
          onClick={onClose}
        >
          Fechar
        </button>
      </div>
    </div>
  );
}
