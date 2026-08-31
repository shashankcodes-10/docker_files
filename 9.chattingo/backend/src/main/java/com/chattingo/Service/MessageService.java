package com.chattingo.Service;

import java.util.List;

import com.chattingo.Exception.ChatException;
import com.chattingo.Exception.MessageException;
import com.chattingo.Exception.UserException;
import com.chattingo.Model.Message;
import com.chattingo.Model.User;
import com.chattingo.Payload.SendMessageRequest;

public interface MessageService {

    public Message sendMessage(SendMessageRequest req) throws UserException, ChatException;

    public List<Message> getChatsMessages(Integer chatId, User reqUser) throws ChatException, UserException;

    public Message findMessageById(Integer messaageId) throws MessageException;

    public void deleteMessage(Integer messageId, User reqUser) throws MessageException;

}
