import { FaUserGraduate } from "react-icons/fa";
import {
  BiSolidUser,
  BiTachometer,
  BiSolidLike,
  BiSolidDislike,
  BiSolidFlagAlt,
} from "react-icons/bi";
import { MdGrade } from "react-icons/md";
import chroma from "chroma-js";
import { useState } from "react";
import postVote from "../api/postVote.js";

export default function Review({ review }) {
  const [upvoted, setUpvoted] = useState(false);
  const [downvoted, setDownvoted] = useState(false);
  const [upvotes, setUpvotes] = useState(review.upvotes);

  function handleUpvote() {
    if (downvoted) return;

    if (upvoted) {
      postVote(review.id, 0).then((newUpvotes) => setUpvotes(newUpvotes));
    } else {
      postVote(review.id, 1).then((newUpvotes) => setUpvotes(newUpvotes));
    }

    setUpvoted(!upvoted);
  }

  function handleDownvote() {
    if (upvoted) return;

    if (downvoted) {
      postVote(review.id, 1).then((newUpvotes) => setUpvotes(newUpvotes));
    } else {
      postVote(review.id, 0).then((newUpvotes) => setUpvotes(newUpvotes));
    }

    setDownvoted(!downvoted);
  }

  return (
    <div class="bg-gray-600 shadow-md shadow-gray-800 shadow- rounded-2xl p-4 m-4 text-white">
      <div class="flex gap-3 items-center">
        <div class="flex gap-1 items-center">
          <BiSolidUser size={25} color={"#000000"} />
          <h3 class="font-semibold text-lg">{review.autor}</h3>
        </div>
        <p class="text-2xl">|</p>
        <div class="flex gap-1 items-center">
          <FaUserGraduate size={22} color={"#000000"} />
          <p class="font-semibold text-lg">{review.professor.nome}</p>
        </div>
      </div>
      <p class="pt-6 italic">{review.comentario}</p>
      <div id="bottom-review-container" class="flex w-full flex-row gap-8 mt-5">
        <div class="flex flex-row items-center gap-1">
          <MdGrade size={20} color="#000000" />
          <p class="font-bold text-lg text-cyan-200">{review.nota}</p>
        </div>
        <div class="flex flex-row items-center gap-1">
          <BiTachometer class="inline" size={30} color={"#000000"} />
          <p class="font-bold text-lg text-cyan-200">{review.dif_disc}</p>
        </div>
        <div class="flex flex-row items-center gap-1">
          <button>
            <BiSolidLike
              id="upvote-button"
              size={20}
              onClick={handleUpvote}
              color={upvoted ? "#17e8ae" : chroma("white")}
            />
          </button>
          <p class="inline text-lg font-bold">{upvotes}</p>
          <button>
            <BiSolidDislike
              size={20}
              onClick={handleDownvote}
              color={downvoted ? chroma("red") : chroma("white")}
            />
          </button>
        </div>
      </div>
    </div>
  );
}
