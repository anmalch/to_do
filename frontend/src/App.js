import './App.css';
import React from "react";
import UserList from "./components/User";
import MenuList from "./components/Menu";
import FooterList from "./components/Footer";
import ProjectList from "./components/Project";
import TodoList from "./components/Todo";
import NotFound404 from "./components/NotFound404";
import axios from "axios";
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom";



class App extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
        'users': [],
        'projects': [],
        'todos': []
    }
  }

  componentDidMount() {

    axios.get('http://127.0.0.1:8000/users/').then(response => {
      this.setState(
        {
          'users':response.data
        }
      )
    }).catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/projects/').then(response => {
      this.setState(
        {
          'projects':response.data
        }
      )
    }).catch(error => console.log(error))
    axios.get('http://127.0.0.1:8000/todos/').then(response => {
      this.setState(
        {
          'todos':response.data
        }
      )
    }).catch(error => console.log(error))



  }


  render() {
    return (
      <div>
          <MenuList menu_items={this.state.menu_items}/>
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
              </nav>
              
                <Routes>
                    <Route exact path='/' element={<UserList users={this.state.users}/>}/>
                    <Route exact path='/projects' element={<ProjectList projects={this.state.projects}/>}/>
                    <Route exact path='/todos' element={<TodoList todos={this.state.todos}/>}/>

                    <Route path='*' element={<NotFound404/>}/>

                </Routes>
          </BrowserRouter>

          <FooterList footer_items={this.state.footer_items}/>
      </div>
    )
  }
}

export default App;
