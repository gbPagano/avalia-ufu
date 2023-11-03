import axios from "axios";
import { root } from "./root.js";

export default class Api {
  static getProfsURL = root + "profs/";
  static getFaculsURL = root + "faculs/";
  static getDiscsURL = root + "discs/";

  static getProfs = async (param) => {
    if (!param) {
      return await axios.get(this.getProfsURL).then((res) => res.data);
    }

    return await axios
      .get(this.getProfsURL + "?sort=" + param)
      .then((res) => res.data);
  };

  static getFaculs = async () => {
    return await axios.get(this.getFaculsURL).then((res) => res.data);
  };

  static getDisc = async (idDisc) => {
    const url = this.getDiscsURL + idDisc;

    return await axios.get(url).then((res) => res.data);
  };

  static getDiscs = async (param) => {
    return param
      ? await axios
          .get(this.getDiscsURL + "?sort=" + param)
          .then((res) => res.data)
      : await axios.get(this.getDiscsURL).then((res) => res.data);
  };

  static postReview = async (autor, prof, discId, reviewContent) => {
    const postReviewURL = root + "reviews/";

    axios
      .post(postReviewURL, {
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
  };

  static postVote = async (reviewId, voteBool) => {
    const apiUrl = root + `reviews/${reviewId}/vote?option=${voteBool}`;

    console.log(apiUrl);

    return await axios
      .post(apiUrl)
      .then((res) => {
        let newUpvotes = res.data.upvotes;
        return newUpvotes;
      })
      .catch((err) => console.log(err));
  };
}
