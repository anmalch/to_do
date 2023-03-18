import React from "react";


const TodoItem = ({todo, delete_todo}) => {

    return (
        <tr>
            <td>{todo.id}</td>
            <td>{todo.user}</td>
            <td>{todo.project}</td>
            <td>{todo.text}</td>
            <td>{todo.created_data}</td>
            <td>{todo.updated_data}</td>

            <td>
                <button onClick={()=>delete_todo(todo.id)} type='button'>Delete</button>
            </td>

        </tr>
    )

}

const TodoList = ({todos, delete_todo}) => {
    return (
        <table>
            <th>Id</th>
            <th>Author</th>
            <th>Project</th>
            <th>text</th>
            <th>created_data</th>
            <th>updated_data</th>
            {todos.map((todo) => <TodoItem todo={todo} delete_todo={delete_todo}/>)}
        </table>
    )
}

export default TodoList