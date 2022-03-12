/* eslint-disable spaced-comment */
/* eslint-disable react/prop-types */
/* eslint-disable no-alert */
/* eslint-disable camelcase */
/* eslint-disable react/jsx-no-bind */
/* eslint-disable react/jsx-filename-extension */
/* eslint-disable react/react-in-jsx-scope */
/* eslint-disable no-shadow */
import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [review, setReview] = useState([]);
  useEffect(() => {
    fetch('/getComments').then((response) => response.json()).then((data) => {
      setReview(data);
    });
  }, []);

  //function is used to delete reviews of the current user on the UI only
  function delete_comment(id) {
    const new_list = review.filter((review) => review.id !== id);

    setReview(new_list);
  }
  //function deletes reviews of the current user from the actual database
  function save_changes(new_reviews) {
    fetch('/save_changes', {
      method: 'POST',
      headers: {
        content_type: 'application/json',
      },
      body: JSON.stringify(new_reviews),
    }).then((response) => response.json());
    alert('Changes have been saved!');
  }
  return (
    <>
      <h1> Your Past Reviews: </h1>
      <List review={review} onDelete={delete_comment} />
      <button type="submit" onClick={() => save_changes(review)}> Save Changes </button>
    </>
  );
}
function List({ review, onDelete }) {
  return (
    <ul>
      {review.map((review) => (
        <Ratings key={review.id} review={review} onDelete={onDelete} />
      ))}
    </ul>
  );
}
function Ratings({ review, onDelete }) {
  return (
    <li>
      <span>
        {' '}
        Movie ID:
        {review.movie_id}
      </span>
      <span>
        {' '}
        Rating:
        {review.ratings}
      </span>
      <span>
        {' '}
        Comment:
        {review.comments}
      </span>
      <button type="button" onClick={() => onDelete(review.id)}>
        Delete
      </button>
    </li>
  );
}

export default App;
