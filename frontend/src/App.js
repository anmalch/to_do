import './App.css';
import React from "react";
import UserList from "./components/User";
import FooterList from "./components/Footer";
import ProjectList from "./components/Project";
import TodoAuthor from "./components/TodoAuthor";
import TodoList from "./components/Todo";
import NotFound404 from "./components/NotFound404";
import Auth from "./components/Auth";
import axios from "axios";
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom";
import LoginForm from "./components/Auth";
import Cookies from "universal-cookie";


class App extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
        'users': [],
        'projects': [],
        'todos': [],
        'token': ''

    }
  }

  logout(){
      this.set_token('')
      this.setState({'users': []})
      this.setState({'projects': []})
      this.setState({'todos': []})
  }

  is_auth(){
    return !!this.state.token
  }

  set_token(token){
      console.log(token)
      const cookies = new Cookies()
      cookies.set('token',token)
      this.setState({'token':token}, ()=>this.load_date())


  }

  get_token_storage(){
      const cookies = new Cookies()
      const token = cookies.get('token')
      this.setState({'token':token}, ()=>this.load_date() )
  }

  get_token(username, password){
      const data = {username: username, password:password}
      axios.post('http://127.0.0.1:8000/api-token-auth/', data).then(response => {
          this.set_token(response.data['token'])
      }).catch(error => alert('Неверный логин или пароль'))

  }

  get_headers(){
      let headers = {
         'Content-Type': 'application/json'
      }
      if (this.is_auth()){
          headers['Authorization'] = 'Token '+this.state.token
      }
      return headers
  }


  load_date() {
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/users/', {headers}).then(response => {
      this.setState(
        {
          'users':response.data
        }
      )
    }).catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/projects/', {headers}).then(response => {
      this.setState(
        {
          'projects':response.data
        }
      )
    }).catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/todos/', {headers}).then(response => {
      this.setState(
        {
          'todos':response.data
        }
      )
    }).catch(error => console.log(error))


  }

  componentDidMount() {
    this.get_token_storage()
  }


  render() {
    return (
      <div>

          <BrowserRouter>
              <nav>
                  <li>
                      <Link to='/'>Authors</Link>
                  </li>
                  <li>
                      <Link to='/projects'>Projects</Link>
                  </li>
                  <li>
                      <Link to='/todos'>Todos</Link>
                  </li>
                  <li>
                      {this.is_auth() ?<button onClick={() => this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
                  </li>
              </nav>
              
                <Routes>
                    <Route exact path='/' element={<Navigate to='/users'/>}/>
                    <Route path='/users'>
                        <Route index element={<UserList users={this.state.users}/>}/>
                        <Route path=':userId' element={<TodoAuthor todo={this.state.todos}/>}/>
                    </Route>
                    <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                    <Route exact path='/todos' element={<TodoList todos={this.state.todos}/>}/>
                    <Route exact path='/login' element={<LoginForm get_token={(username, password) =>
                    this.get_token(username, password)}/>}/>

                    <Route path='*' element={<NotFound404/>}/>

                </Routes>
          </BrowserRouter>

          <FooterList footer_items={this.state.footer_items}/>
      </div>
    )
  }
}

export default App;
