import logo from './logo.svg';
import './App.css';
import React from "react";
import UserList from "./components/User";
import MenuList from "./components/Menu";
import FooterList from "./components/Footer";
import axios from "axios";


class App extends React.Component{
  constructor(props) {
    super(props);
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
    axios.get('http://127.0.0.1:8000/api/users/').then(response => {
      this.setState(
        {
          'users':response.data
        }
      )
    }).catch(error => console.log(error))

  }


  render() {
    return (
      <div>
        <MenuList menu_items={this.state.menu_items}/>
        <UserList users={this.state.users}/>
        <FooterList footer_items={this.state.footer_items}/>

      </div>
    )
  }
}

export default App;
