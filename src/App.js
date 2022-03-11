import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [review, setReview] = useState([]);
  useEffect(() => {
    fetch('/getComments').then(response => response.json()).then(data => {
      setReview(data);
    });
  }, [])

  function delete_comment(id) {
    const new_list = review.filter((review) => review.id !== id);

    setReview(new_list);
  }
  return <List review={review} onRemove={delete_comment} />;
};
const List = ({ review, onRemove }) => (
  <ul>
    {review.map((review) => (
      <Ratings key={review.id} review={review} onRemove={onRemove} />
    ))}
  </ul>
);
const Ratings = ({ review, onRemove }) => (
  <li>
    <span> Movie ID: {review.movie_id} </span>
    <span> Rating: {review.ratings} </span>
    <span> Comment: {review.comments} </span>
    <button type="button" onClick={() => onRemove(review.id)}>
      Delete
    </button>
  </li>
);

export default App;
