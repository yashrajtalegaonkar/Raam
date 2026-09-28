import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QPushButton, QLabel, QGroupBox, QScrollArea
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from helpline_ai import get_ai_response
from tts_engine import text_to_speech
from stt_engine import speech_to_text


class HelplineUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Road Emergency Helpline + Car Simulator")
        self.setGeometry(200, 100, 900, 750)
        
        # Set application font
        app_font = QFont("Segoe UI", 10)
        self.setFont(app_font)
        
        # Conversation history
        self.conversation_history = []
        
        self.init_ui()
        self.apply_styles()

    def init_ui(self):
        main_layout = QVBoxLayout()
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # Header
        header = QLabel("AI ROAD EMERGENCY HELPLINE")
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        header.setFont(QFont("Segoe UI", 18, QFont.Weight.Bold))
        header.setStyleSheet("color: #000000; padding: 15px;")
        main_layout.addWidget(header)

        # Emergency Input Section
        input_label = QLabel("Describe Your Emergency")
        input_label.setFont(QFont("Segoe UI", 11, QFont.Weight.DemiBold))
        input_label.setStyleSheet("color: #333333; padding: 5px 0;")

        self.input_box = QTextEdit()
        self.input_box.setPlaceholderText("Type or speak your emergency here...")
        self.input_box.setMinimumHeight(100)
        self.input_box.setMaximumHeight(100)

        # Action Buttons
        button_layout = QHBoxLayout()
        button_layout.setSpacing(15)

        self.speak_btn = QPushButton("🎤 Voice Input")
        self.speak_btn.clicked.connect(self.handle_speech_input)
        self.speak_btn.setMinimumHeight(45)
        self.speak_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.send_btn = QPushButton("Get Help")
        self.send_btn.clicked.connect(self.process_query)
        self.send_btn.setMinimumHeight(45)
        self.send_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.clear_btn = QPushButton("🔄 Clear/New Emergency")
        self.clear_btn.clicked.connect(self.clear_inputs)
        self.clear_btn.setMinimumHeight(45)
        self.clear_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        button_layout.addWidget(self.speak_btn)
        button_layout.addWidget(self.send_btn)
        button_layout.addWidget(self.clear_btn)

        # Response Section
        response_label = QLabel("Helpline Response & History")
        response_label.setFont(QFont("Segoe UI", 11, QFont.Weight.DemiBold))
        response_label.setStyleSheet("color: #333333; padding: 5px 0;")

        self.response_box = QTextEdit()
        self.response_box.setReadOnly(True)
        self.response_box.setMinimumHeight(250)

        main_layout.addWidget(input_label)
        main_layout.addWidget(self.input_box)
        main_layout.addLayout(button_layout)
        main_layout.addWidget(response_label)
        main_layout.addWidget(self.response_box)

        # Car Simulator Section
        car_group = QGroupBox("Car Simulator - Trigger Failures")
        car_group.setFont(QFont("Segoe UI", 11, QFont.Weight.DemiBold))
        car_layout = QHBoxLayout()
        car_layout.setSpacing(15)

        self.engine_fail_btn = QPushButton("Engine Failure")
        self.engine_fail_btn.clicked.connect(
            lambda: self.trigger_car_failure("Engine failure detected! Car stopped on the highway.")
        )
        self.engine_fail_btn.setMinimumHeight(45)
        self.engine_fail_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.tire_burst_btn = QPushButton("Tire Burst")
        self.tire_burst_btn.clicked.connect(
            lambda: self.trigger_car_failure("Tire burst on highway! Vehicle cannot move.")
        )
        self.tire_burst_btn.setMinimumHeight(45)
        self.tire_burst_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.brake_fail_btn = QPushButton("Brake Failure")
        self.brake_fail_btn.clicked.connect(
            lambda: self.trigger_car_failure("Brake failure! Cannot stop the car safely.")
        )
        self.brake_fail_btn.setMinimumHeight(45)
        self.brake_fail_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.accident_btn = QPushButton("Accident Detected")
        self.accident_btn.clicked.connect(
            lambda: self.trigger_car_failure("Car accident occurred! Immediate help needed.")
        )
        self.accident_btn.setMinimumHeight(45)
        self.accident_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        car_layout.addWidget(self.engine_fail_btn)
        car_layout.addWidget(self.tire_burst_btn)
        car_layout.addWidget(self.brake_fail_btn)
        car_layout.addWidget(self.accident_btn)

        car_group.setLayout(car_layout)
        main_layout.addWidget(car_group)

        self.setLayout(main_layout)

    def apply_styles(self):
        """Apply clean white and black theme"""
        
        self.setStyleSheet("""
            QWidget {
                background-color: #FFFFFF;
                color: #000000;
            }
            
            QTextEdit {
                background-color: #FAFAFA;
                border: 2px solid #E0E0E0;
                border-radius: 8px;
                padding: 12px;
                color: #000000;
                font-size: 10pt;
            }
            
            QTextEdit:focus {
                border: 2px solid #333333;
            }
            
            QPushButton {
                background-color: #000000;
                color: #FFFFFF;
                border: none;
                border-radius: 6px;
                padding: 12px 24px;
                font-size: 10pt;
                font-weight: 600;
            }
            
            QPushButton:hover {
                background-color: #333333;
            }
            
            QPushButton:pressed {
                background-color: #555555;
            }
            
            QGroupBox {
                background-color: #F5F5F5;
                border: 2px solid #E0E0E0;
                border-radius: 10px;
                margin-top: 15px;
                padding-top: 20px;
                font-weight: 600;
                color: #000000;
            }
            
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 5px 15px;
                color: #000000;
            }
            
            QLabel {
                color: #000000;
            }
        """)

    def clear_inputs(self):
        """Clear input box only, keeping the conversation history"""
        self.input_box.clear()
        self.input_box.setFocus()
        
    def clear_all(self):
        """Clear everything including history"""
        self.input_box.clear()
        self.response_box.clear()
        self.conversation_history.clear()
        self.input_box.setFocus()

    def handle_speech_input(self):
        """Handle voice input from user"""
        self.response_box.append("\n🎤 Listening... Please speak clearly.\n")
        QApplication.processEvents()
        
        try:
            spoken_text = speech_to_text()
            self.input_box.setText(spoken_text)
            self.response_box.append(f"✓ Speech captured: '{spoken_text}'\n")
            QApplication.processEvents()
            # Automatically process the query after speech input
            self.process_query()
        except Exception as e:
            self.response_box.append(
                f"❌ Could not capture speech. Please try again or type your emergency.\nError: {str(e)}\n"
            )

    def process_query(self):
        """Process user emergency query"""
        user_text = self.input_box.toPlainText().strip()
        if not user_text:
            self.response_box.append("⚠️ Please describe your emergency before requesting help.\n")
            return

        # Add separator for new query
        if self.conversation_history:
            self.response_box.append("\n" + "="*60 + "\n")
        
        self.response_box.append(f"📝 YOUR EMERGENCY: {user_text}\n")
        self.response_box.append("⏳ Processing emergency request...\n")
        QApplication.processEvents()

        try:
            ai_response = get_ai_response(user_text)
            
            # Display response
            self.response_box.append(f"\n🚨 EMERGENCY ASSESSMENT:\n{'-' * 50}\n")
            self.response_box.append(ai_response)
            self.response_box.append(f"\n{'-' * 50}\n")
            
            # Store in history
            self.conversation_history.append({
                'query': user_text,
                'response': ai_response
            })
            
            # Generate voice response
            text_to_speech(ai_response)
            
            # Clear input for next query
            self.input_box.clear()
            self.input_box.setFocus()
            
        except Exception as e:
            self.response_box.append(f"❌ Error processing request: {str(e)}\n")

    def trigger_car_failure(self, failure_text: str):
        """
        Simulate car failure, send to chat, and notify demo services
        """
        # Add separator for new emergency
        if self.conversation_history or self.response_box.toPlainText():
            self.response_box.append("\n" + "="*60 + "\n")
        
        self.input_box.setText(failure_text)
        self.response_box.append(f"🚗 SYSTEM ALERT: {failure_text}\n\n")
        self.response_box.append("📡 Notifying emergency services...\n")
        QApplication.processEvents()

        try:
            # Send to AI
            ai_response = get_ai_response(failure_text)
            
            self.response_box.append(f"\n🤖 AI HELPLINE RESPONSE:\n{'-' * 50}\n")
            self.response_box.append(ai_response)
            self.response_box.append(f"\n{'-' * 50}\n")
            
            # Demo notifications
            self.response_box.append("\n📞 SERVICE NOTIFICATIONS:\n")
            self.response_box.append("  ✓ Nearby garage notified (demo)\n")
            self.response_box.append("  ✓ Medical services alerted (demo)\n")
            self.response_box.append("  ✓ Location shared with authorities (demo)\n")
            
            # Store in history
            self.conversation_history.append({
                'query': failure_text,
                'response': ai_response,
                'type': 'car_failure'
            })
            
            # Generate voice response
            text_to_speech(ai_response)
            
            # Clear input for next query
            self.input_box.clear()
            self.input_box.setFocus()
            
        except Exception as e:
            self.response_box.append(f"❌ Error processing car failure: {str(e)}\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelplineUI()
    window.show()
    sys.exit(app.exec())