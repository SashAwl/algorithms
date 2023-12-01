public class ListOne {
    Node head;

    public void addFirst(int value){
        Node node = new Node();
        node.value = value;
        node.next = head;
        head = node;
    }

    public void addLast(int value){
        Node node = new Node();
        node.value = value;
        if (head == null){
            head = node;
        } else {
            Node currentNode = head;
            while (currentNode.next != null){
                currentNode = currentNode.next;
            }
            currentNode.next = node;
        }
    }

    public void removeFirst(){
        if (head != null){
            head = head.next;
        }
    }

    public void removeLast(){
        if (head != null){
            Node currentNode = head;
            while (currentNode.next != null){
                if (currentNode.next.next == null){
                    currentNode.next = null;
                    return;
                }
                currentNode = currentNode.next;
            }
        }
    }

    public  boolean contains(int value){
        Node node = head;
        while (node != null){
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
    }
}
