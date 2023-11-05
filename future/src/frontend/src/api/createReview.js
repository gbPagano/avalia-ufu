import axios from "axios";
import { root } from "./root.js";

export default async function createReview(autor, prof, discId, reviewContent) {
  const createReviewAPI_URL = root + "reviews/";

  console.log("autor", autor);
  console.log("prof", prof);
  console.log("discId", discId);
  console.log("reviewContent", reviewContent);

  axios
    .post(createReviewAPI_URL, {
      id_prof: prof.id,
      id_disc: discId,
      autor: autor,
      comentario: reviewContent.comment,
      nota: reviewContent.profScore,
      dif_disc: reviewContent.discDifficulty,
      upvotes: 0,
    })
    .then((res) => {
      return res;
    })
    .catch((err) => {
      console.log(err);
    });
}
