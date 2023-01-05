public class ListTwo {
    Node head;
    Node tail;

    public void revert(){
        Node currentNode = head;
        while(currentNode != null){
            Node next = currentNode.next;
            Node previous = currentNode.previous;

            currentNode.next = previous;
            currentNode.previous = next;

            if (previous == null){
                tail = currentNode;
            }
            if (next == null) {
                head = currentNode;
            }
            currentNode = next;
        }
    }

    public void addFirst(int value){
        Node node = new Node();
        node.value = value;
        if (head != null){
            node.next = head;
            head.previous = node;
        } else {
            tail = node;
        }
        head = node;
    }

    public void addLast(int value){
        Node node = new Node();
        node.value = value;
        if (tail != null){
            tail.next = node;
            node.previous = tail;
        } else {
            head = node;
        }
        tail = node;
    }

    public void removeFirst(){
        if (head != null && head.next != null){
            head.next.previous = null;
            head = head.next;
        } else {
            head = null;
            tail = null;
        }
    }

    public void removeLast(){
        if (tail != null && tail.previous != null){
            tail.previous.next = null;
            tail = tail.previous;
        } else {
            head = null;
            tail = null;
        }
    }

    public  boolean contains(int value) {
        Node node = head;
        while (node != null) {
            if (node.value == value) {
                return true;
            }
            node = node.next;
        }
        return false;
    }

    public class Node {
        int value;
        Node next;
        Node previous;
    }
}
