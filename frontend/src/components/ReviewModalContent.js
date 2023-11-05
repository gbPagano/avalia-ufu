import Review from "./Review";

export default function ReviewModalContent({ nomeDisc, reviews, onClose }) {
  return (
    <div
      id="review-modal"
      class="font-custom text-white fixed flex flex-col justify-between top-1/2 left-1/2 -translate-y-1/2 -translate-x-1/2 pt-5 pb-10 pl-6 pr-6 backdrop-blur-xl bg-gray-950 bg-opacity-70 z-10000 shadow-xl shadow-gray-800 w-1/2 h-3/4 rounded-2xl"
    >
      <div id="reviews-portal-container" class="w-full overflow-y-scroll">
        <div class="pb-3">
          <h2 class="inline">Reviews de </h2>
          <h2 class="inline text-cyan-500 font-bold text-xl">{nomeDisc}</h2>
        </div>
        <div class="w-full">
          {reviews !== undefined ? (
            reviews.map((review) => <Review review={review} />)
          ) : (
            <></>
          )}
        </div>
      </div>
      <div id="btn-fechar-container" class="flex justify-end w-full py-5">
        <button
          class="absolute px-5 py-2 text-sm text-white font-semibold rounded-full border-blue-700 bg-cyan-600 hover:bg-cyan-900"
          onClick={onClose}
        >
          Fechar
        </button>
      </div>
    </div>
  );
}
