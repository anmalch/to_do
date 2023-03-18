import React from "react";
import {useParams} from "react-router-dom";


const TodoItem = ({todo}) => {

    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.user}</td>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.created_data}</td>
            <td>{todo.updated_data}</td>

        </tr>
    )

}

const TodoAuthor = ({todos}) => {
    let {userId} = useParams()
    let filter_todos = todos.filter((todo)=> todo.users.includes(parseInt(userId)))
    return (
        <table>
            <th>Id</th>
            <th>Author</th>
            <th>Project</th>
            <th>text</th>
            <th>created_data</th>
            <th>updated_data</th>
            {todos.map((todo) => <TodoItem todo={todo}/>)}
        </table>
    )
}

export default TodoAuthor