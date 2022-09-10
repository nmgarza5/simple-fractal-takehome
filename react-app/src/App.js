import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Display from './components/Display';
import Form from './components/Form';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path='/' >
          <h1>Engineer Percentile Lookup</h1>
          <Form />
          <Display />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
