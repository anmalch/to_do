import React from "react";


const TodoItem = ({todo}) => {

    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.author}</td>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.created_data}</td>
            <td>{todo.updated_data}</td>

        </tr>
    )

}

const TodoList = ({todos}) => {
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

export default TodoList