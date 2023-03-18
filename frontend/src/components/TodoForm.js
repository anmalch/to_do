import React from "react";


class TodoForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {"name": '', "users": []}
    }

    handleChange(event){
        this.setState(
            {
                [event.target.name] : event.target.value
            }
        )

    }

    handleAuthorChange(event) {
        if(!event.target.selectedOptions) {
            this.setState({
                'users': []
            })
            return;
        }
        let users = []
        for(let i = 0; i < event.target.selectedOptions.length; i++){
            users.push(event.target.selectedOptions.item(i).value)
        }
        this.setState(
            {'users':users}
        )
    }
    handleSubmit(event){
        this.props.create_todo(this.state.name, this.state.users)
        event.preventDefault()
    }
    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label htmlFor="name"></label>
                    <input type="text" name="name" placeholder="name"
                           value={this.state.name} onChange={(event)=>this.handleChange(event)} />
                </div>
                <select name="users" multiple onChange={(event) => this.handleAuthorChange(event)}>
                    {this.props.users.map((item)=> <option value={item.id}>{item.last_name}</option>)}
                </select>

                <input type="submit" value="Save" />
            </form>
        );
    }
}

export default TodoForm