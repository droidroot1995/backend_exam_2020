import React from 'react';
import {Switch, Route, Redirect} from 'react-router-dom'
import AuthForm from './AuthForm'
import '../styles/App.css';

function App() {
  return (
    <Switch>
      <Route path='/plist' render={() => null}/>
      <Route path='/login' render={() =><AuthForm/>}/>
      <Redirect to='/login'/>
    </Switch>
  );
}

export default App;
