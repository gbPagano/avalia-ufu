import { root } from "./root.js";
import axios from "axios";

export default async function postVote(reviewId, voteBool) {
  const apiUrl = root + `reviews/${reviewId}/vote?option=${voteBool}`;

  console.log(apiUrl);

  return await axios
    .post(apiUrl)
    .then((res) => {
      let newUpvotes = res.data.upvotes;
      // console.log(`postVotes newUpotes: ${newUpvotes}`);
      return newUpvotes;
    })
    .catch((err) => console.log(err));
}
