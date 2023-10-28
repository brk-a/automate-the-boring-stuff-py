import { createContext, useState, useEffect } from "react";

export const TaskContext = createContext()
export const TaskProvider = ({children}) => {
    const [viewCompleted, setViewCompleted] = useState(false)
  const [displayCompleted, setDisplayCompleted] = useState(false)
  const [taskList, setTaskList] = useState([])
  const [newItem, setNewItem] = useState([])

  const handleViewCompleted = () => {
    setViewCompleted(!viewCompleted)
  }
  const handleDisplayCompleted = () => {
    setDisplayCompleted(!displayCompleted)
  }

  const handleNewItems = () => {
    const newItems = taskList.filter(item => item.completed == viewCompleted)
    setNewItem(newItems)
  }
  useEffect(() => {
    handleNewItems()
  }, [])

  return(
    <TaskContext.Provider value={{
        viewCompleted,
        displayCompleted,
        taskList,
        newItem,
        handleViewCompleted,
        handleDisplayCompleted,
        handleNewItems,
    }}
    >
        {children}
    </TaskContext.Provider>
  )
}