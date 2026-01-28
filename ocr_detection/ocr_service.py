# -*- coding: utf-8 -*-
"""
@Time : 2025/1/22 18:02
@Email : Lvan826199@163.com
@公众号 : 梦无矶测开实录
@File : ocr_service.py
"""
__author__ = "梦无矶小仔"

# ocr_service.py
import traceback

from fastapi import FastAPI, HTTPException
import time

# ocr_service.py
from fastapi import FastAPI, HTTPException
from ocr_detection.target_detection import *
from PIL import Image
import logging
import uvicorn

# 初始化日志
logging.basicConfig(level=logging.INFO)

# 初始化 FastAPI 应用
app = FastAPI()

# 在应用启动时初始化 OCR 模块
ocr_engine = None


@app.on_event("startup")
async def startup_event():
    global ocr_engine
    logging.info("正在初始化 OCR 模块...")
    # 这里假设 ocr_engine 是一个 OCR 模块实例
    ocr_engine = OCRSingleton()  # 可以替换为其他 OCR 实例，如 PaddleOCR
    logging.info("OCR 模块初始化完成。")


def process_ocr(image_path: str) -> str:
    """使用 OCR 模块处理图像"""
    try:
        logging.info(f"处理图像：{image_path}")
        # image = Image.open(image_path)
        action_text = {"1": 0}
        result = ocr_engine.ocr_exist(img=image_path, action_text=action_text)
        return result
    except Exception as e:
        logging.error(f"处理图像时出错：{e}")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="OCR 处理失败")


@app.get("/ocr")
async def ocr(image_path: str):
    """OCR 处理接口"""
    if not image_path:
        raise HTTPException(status_code=400, detail="Image path is required")

    result = process_ocr(image_path)
    return {"result": result}


if __name__ == "__main__":

    uvicorn.run(app, host="127.0.0.1", port=8666)

