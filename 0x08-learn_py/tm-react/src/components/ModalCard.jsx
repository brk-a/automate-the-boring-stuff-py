import { useState } from 'react'
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label
} from 'reactstrap'

const ModalCard = () => {
    const [activeItem, setActiveItem] = useState({})
    const [toggle, setToggle] = useState(false)
    const [task, setTask] = useState([])

    const handleChangeCheckbox = (e) => {
        const { name, value } = e.target
        if (e.target.type === "checkbox") {
            value = e.target.checked
        }
        const activItem = { ...activeItem, name: value }
        setActiveItem(activItem)
    }
    const handleToggle = () => {
        setToggle(!toggle)
    }
    const handleSetTask = (e) => {
        setTask(e.target.value)
    }
    return (
        <Modal isOpen={toggle} toggle={handleToggle}>
            <ModalHeader>Task item</ModalHeader>
            <ModalBody>
                <Form>
                    <FormGroup>
                        <Label for='title'>Title</Label>
                        <Input
                            type='text'
                            name='title'
                            value={activeItem.title}
                            onChange={handleChangeCheckbox}
                            placeholder='Enter task title'
                        />
                    </FormGroup>
                    <FormGroup>
                        <Label for='description'>Description</Label>
                        <Input
                            type='text'
                            name='description'
                            value={activeItem.description}
                            onChange={handleChangeCheckbox}
                            placeholder='Enter task description'
                        />
                    </FormGroup>
                    <FormGroup check>
                        <Label for='completed'>
                            <Input
                                type='checkbox'
                                name='completed'
                                value={activeItem.completed}
                                onChange={handleChangeCheckbox}
                                placeholder='Enter task title'
                            />
                            Completed
                        </Label>
                    </FormGroup>
                </Form>
            </ModalBody>
            <ModalFooter>
                <Button color='success' onClick={handleSetTask}>
                    Save
                </Button>
            </ModalFooter>
        </Modal>
    )
}

export default ModalCard